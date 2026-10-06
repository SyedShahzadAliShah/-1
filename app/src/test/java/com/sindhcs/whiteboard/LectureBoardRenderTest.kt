package com.sindhcs.whiteboard

import android.graphics.Bitmap
import android.graphics.Canvas
import android.view.View.MeasureSpec
import androidx.test.core.app.ApplicationProvider
import com.sindhcs.whiteboard.data.CatalogStore
import com.sindhcs.whiteboard.whiteboard.WhiteboardView
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode
import java.io.File
import java.io.FileOutputStream

@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34])
@GraphicsMode(GraphicsMode.Mode.NATIVE)
class LectureBoardRenderTest {

    @Test
    fun catalogCoversBothGradesAndBoardsDraw() {
        val context = ApplicationProvider.getApplicationContext<android.content.Context>()
        val catalog = CatalogStore.get(context)
        assertTrue(catalog.grades.size == 2)
        assertTrue(catalog.grade("xi").lectureCount >= 20)
        assertTrue(catalog.grade("xii").lectureCount >= 20)
        catalog.grades.flatMap { it.chapters }.flatMap { it.lectures }.forEach { lecture ->
            assertTrue(lecture.boards.size >= 3)
            lecture.boards.forEach { board ->
                assertTrue(board.narration.split(Regex("\\s+")).size >= 28)
                assertTrue(board.marks.first().k == "title")
            }
        }

        val samples = listOf(
            "xi-truth" to 1,
            "xi-kmap" to 1,
            "xi-sort" to 1,
            "xi-osi" to 0,
            "xii-linear-ds" to 1,
            "xii-stats" to 0
        )
        val outDir = File("/opt/cursor/artifacts")
        outDir.mkdirs()
        samples.forEach { (lectureId, boardIndex) ->
            val lecture = catalog.lecture(lectureId)
            val bitmap = render(lecture.boards[boardIndex].marks)
            FileOutputStream(File(outDir, "board-$lectureId-$boardIndex.png")).use { stream ->
                bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream)
            }
            assertTrue(bitmap.width > 0 && bitmap.height > 0)
        }
    }

    private fun render(marks: List<com.sindhcs.whiteboard.data.Mark>): Bitmap {
        val context = ApplicationProvider.getApplicationContext<android.content.Context>()
        val view = WhiteboardView(context)
        val width = 1080
        val height = 1600
        view.measure(
            MeasureSpec.makeMeasureSpec(width, MeasureSpec.EXACTLY),
            MeasureSpec.makeMeasureSpec(height, MeasureSpec.EXACTLY)
        )
        view.layout(0, 0, width, height)
        view.submit(marks)
        view.showFinished()
        val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        view.draw(Canvas(bitmap))
        return bitmap
    }
}
