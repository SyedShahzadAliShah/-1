package pk.edu.biek.cslectures.data

import pk.edu.biek.cslectures.model.Lecture

object Catalog {
    val lectures: List<Lecture> = xiLectures() + xiiLectures()

    fun find(id: String): Lecture = lectures.first { it.id == id }
}
