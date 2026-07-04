package com.pakrecipes.cooking

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.pakrecipes.cooking.data.CityCategory
import com.pakrecipes.cooking.data.RecipeRepository
import com.pakrecipes.cooking.databinding.ActivityMainBinding
import com.pakrecipes.cooking.ui.CityAdapter
import com.pakrecipes.cooking.ui.RecipeAdapter
import com.pakrecipes.cooking.util.PdfExporter
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var recipeAdapter: RecipeAdapter
    private lateinit var cityAdapter: CityAdapter
    private var selectedCity = CityCategory.ALL

    override fun attachBaseContext(newBase: Context) {
        super.attachBaseContext(RecipeApp.applyUrduLocale(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.title = getString(R.string.app_name)

        setupCityList()
        setupRecipeList()
        updateRecipeList()
    }

    private fun setupCityList() {
        cityAdapter = CityAdapter { cityId ->
            selectedCity = cityId
            updateRecipeList()
        }
        binding.cityList.layoutManager =
            LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        binding.cityList.adapter = cityAdapter
        cityAdapter.submitList(CityCategory.all())
    }

    private fun setupRecipeList() {
        recipeAdapter = RecipeAdapter { recipe ->
            startActivity(
                Intent(this, RecipeDetailActivity::class.java).apply {
                    putExtra(RecipeDetailActivity.EXTRA_RECIPE_ID, recipe.id)
                }
            )
        }
        binding.recipeList.layoutManager = LinearLayoutManager(this)
        binding.recipeList.adapter = recipeAdapter
    }

    private fun updateRecipeList() {
        val recipes = RecipeRepository.getByCity(selectedCity)
        recipeAdapter.submitList(recipes)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_export_all -> {
                exportAllRecipes()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun exportAllRecipes() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportAllRecipes(this@MainActivity)
                }
                PdfExporter.showExportActions(this@MainActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@MainActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }
}
