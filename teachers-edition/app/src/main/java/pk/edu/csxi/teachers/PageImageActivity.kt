package pk.edu.csxi.teachers

import android.graphics.drawable.BitmapDrawable
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import pk.edu.csxi.teachers.databinding.ActivityPageImageBinding

/** Shows the original page layout (English only, Urdu removed) so diagrams can be studied zoomed in. */
class PageImageActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = ActivityPageImageBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val page = intent.getIntExtra(ReaderActivity.EXTRA_PAGE, 1)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        title = getString(R.string.page_layout_title, page)
        val bmp = ContentRepository(this).pageBitmap(page)
        binding.image.setImageDrawable(bmp?.let { BitmapDrawable(resources, it) })
        binding.hint.setOnClickListener { binding.hint.animate().alpha(0f).withEndAction { binding.hint.visibility = android.view.View.GONE } }
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
