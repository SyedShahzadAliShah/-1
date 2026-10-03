package pk.edu.csxi.teachers

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.media.AudioManager
import android.os.Bundle
import android.text.InputType
import android.view.LayoutInflater
import android.view.Menu
import android.view.MenuItem
import android.view.ViewGroup
import android.view.WindowManager
import android.widget.EditText
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.viewpager2.widget.ViewPager2
import pk.edu.csxi.teachers.databinding.ActivityReaderBinding
import pk.edu.csxi.teachers.databinding.ItemPageBinding

class ReaderActivity : AppCompatActivity(), Narrator.Listener {

    companion object {
        const val EXTRA_PAGE = "page"
        private val SPEEDS = floatArrayOf(0.75f, 1.0f, 1.25f, 1.5f)
    }

    private lateinit var binding: ActivityReaderBinding
    private lateinit var repo: ContentRepository
    private lateinit var prefs: Prefs
    private lateinit var narrator: Narrator
    private val adapters = HashMap<Int, BlockAdapter>()
    private var pendingAutoPlay = false
    private var activePage = -1
    private var noisyRegistered = false

    private val noisyReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            if (intent?.action == AudioManager.ACTION_AUDIO_BECOMING_NOISY) narrator.pause()
        }
    }

    private val currentPage get() = binding.pager.currentItem + 1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityReaderBinding.inflate(layoutInflater)
        setContentView(binding.root)
        repo = ContentRepository(this)
        prefs = Prefs(this)
        narrator = Narrator(this, this).also { it.speed = prefs.speed }

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        val start = intent.getIntExtra(EXTRA_PAGE, 1).coerceIn(1, repo.pageCount)
        binding.pager.adapter = PagerAdapter()
        binding.pager.offscreenPageLimit = 1
        binding.pager.setCurrentItem(start - 1, false)
        binding.pager.registerOnPageChangeCallback(object : ViewPager2.OnPageChangeCallback() {
            override fun onPageSelected(position: Int) = onPageChanged(position + 1)
        })
        onPageChanged(start)

        binding.playButton.setOnClickListener { togglePlayback() }
        binding.prevButton.setOnClickListener { goTo(currentPage - 1) }
        binding.nextButton.setOnClickListener { goTo(currentPage + 1) }
        binding.speedButton.setOnClickListener { cycleSpeed() }
        updateSpeedLabel()
        onPlayingChanged(false)
    }

    override fun onStart() {
        super.onStart()
        if (!noisyRegistered) {
            registerReceiver(noisyReceiver, IntentFilter(AudioManager.ACTION_AUDIO_BECOMING_NOISY))
            noisyRegistered = true
        }
    }

    override fun onStop() {
        super.onStop()
        if (noisyRegistered) {
            unregisterReceiver(noisyReceiver)
            noisyRegistered = false
        }
    }

    override fun onDestroy() {
        narrator.release()
        super.onDestroy()
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_reader, menu)
        menu.findItem(R.id.action_auto).isChecked = prefs.autoAdvance
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean = when (item.itemId) {
        android.R.id.home -> { finish(); true }
        R.id.action_page_view -> { openPageView(); true }
        R.id.action_goto -> { showGoToDialog(); true }
        R.id.action_auto -> {
            item.isChecked = !item.isChecked
            prefs.autoAdvance = item.isChecked
            true
        }
        else -> super.onOptionsItemSelected(item)
    }

    private fun openPageView() {
        startActivity(Intent(this, PageImageActivity::class.java).putExtra(EXTRA_PAGE, currentPage))
    }

    private fun showGoToDialog() {
        val input = EditText(this).apply {
            inputType = InputType.TYPE_CLASS_NUMBER
            hint = getString(R.string.go_to_hint, repo.pageCount)
        }
        AlertDialog.Builder(this)
            .setTitle(R.string.go_to_page)
            .setView(input)
            .setPositiveButton(android.R.string.ok) { _, _ ->
                input.text.toString().toIntOrNull()?.let { goTo(it) }
            }
            .setNegativeButton(android.R.string.cancel, null)
            .show()
    }

    private fun goTo(page: Int) {
        if (page !in 1..repo.pageCount) return
        binding.pager.setCurrentItem(page - 1, true)
    }

    private fun onPageChanged(page: Int) {
        val chapter = repo.chapterOf(page)
        binding.toolbar.title = getString(R.string.chapter_n, chapter.n) + " \u00b7 " + chapter.title
        binding.toolbar.subtitle = repo.info(page).heads.firstOrNull()
        binding.pageIndicator.text = getString(R.string.page_of, page, repo.pageCount)
        binding.prevButton.isEnabled = page > 1
        binding.nextButton.isEnabled = page < repo.pageCount
        prefs.lastPage = page

        if (pendingAutoPlay || (narrator.isPlaying && narrator.currentPage != page)) {
            pendingAutoPlay = false
            binding.pager.post { playFrom(page, 0) }
        } else if (narrator.hasSession && narrator.currentPage != page) {
            narrator.stop()
            highlight(-1, -1)
        }
    }

    private fun togglePlayback() {
        when {
            narrator.isPlaying -> narrator.pause()
            narrator.hasSession && narrator.currentPage == currentPage -> narrator.resume()
            else -> playFrom(currentPage, 0)
        }
    }

    private fun playFrom(page: Int, pos: Int) {
        narrator.play(page, repo.items(page), pos)
    }

    private fun cycleSpeed() {
        val i = SPEEDS.indexOfFirst { it == prefs.speed }
        val next = SPEEDS[(i + 1) % SPEEDS.size]
        prefs.speed = next
        narrator.speed = next
        updateSpeedLabel()
    }

    private fun updateSpeedLabel() {
        val s = prefs.speed
        binding.speedButton.text = (if (s == s.toInt().toFloat()) "${s.toInt()}.0" else s.toString()) + "\u00d7"
    }

    private fun highlight(page: Int, pos: Int) {
        if (activePage != page && activePage > 0) adapters[activePage]?.setActive(-1)
        activePage = page
        if (page > 0) adapters[page]?.setActive(pos)
    }

    private fun scrollTo(page: Int, pos: Int) {
        val pagerRv = binding.pager.getChildAt(0) as RecyclerView
        val holder = pagerRv.findViewHolderForAdapterPosition(page - 1) as? PageHolder ?: return
        val lm = holder.b.list.layoutManager as LinearLayoutManager
        if (pos < lm.findFirstCompletelyVisibleItemPosition() || pos > lm.findLastCompletelyVisibleItemPosition()) {
            lm.scrollToPositionWithOffset(pos, holder.b.list.height / 5)
        }
    }

    override fun onItemStarted(page: Int, position: Int) {
        highlight(page, position)
        scrollTo(page, position)
    }

    override fun onPageFinished(page: Int) {
        highlight(-1, -1)
        if (prefs.autoAdvance && page < repo.pageCount && page == currentPage) {
            pendingAutoPlay = true
            goTo(page + 1)
        }
    }

    override fun onPlayingChanged(playing: Boolean) {
        binding.playButton.setIconResource(if (playing) R.drawable.ic_pause else R.drawable.ic_play)
        binding.playButton.contentDescription = getString(if (playing) R.string.pause else R.string.play_urdu)
        if (playing) window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        else window.clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
    }

    private inner class PagerAdapter : RecyclerView.Adapter<PageHolder>() {
        override fun getItemCount() = repo.pageCount

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PageHolder {
            val b = ItemPageBinding.inflate(LayoutInflater.from(parent.context), parent, false)
            b.list.layoutManager = LinearLayoutManager(parent.context)
            return PageHolder(b)
        }

        override fun onBindViewHolder(holder: PageHolder, position: Int) {
            val page = position + 1
            val items = repo.items(page)
            val adapter = BlockAdapter(items, { pos -> playFrom(page, pos) }, { openPageView() })
            adapters[page] = adapter
            holder.page = page
            holder.b.list.adapter = adapter
            holder.b.list.scrollToPosition(0)
            if (page == activePage) adapter.setActive(narrator.currentPosition)
        }

        override fun onViewRecycled(holder: PageHolder) {
            if (adapters[holder.page]?.let { holder.b.list.adapter === it } == true) adapters.remove(holder.page)
        }
    }

    private class PageHolder(val b: ItemPageBinding) : RecyclerView.ViewHolder(b.root) {
        var page = 0
    }
}
