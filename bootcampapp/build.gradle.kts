plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

val bootcampAssets = layout.buildDirectory.dir("generated/bootcampAssets")

val copyBootcampWeb = tasks.register<Copy>("copyBootcampWeb") {
    from(rootProject.file("bootcamp")) {
        include("index.html", "css/**", "js/**", "vendor/**")
    }
    into(bootcampAssets.map { it.dir("www") })
}

android {
    namespace = "com.selftaught.csbootcamp"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.selftaught.csbootcamp"
        minSdk = 24
        targetSdk = 34
        versionCode = 6
        versionName = "1.5.0"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    sourceSets.getByName("main").assets.srcDir(bootcampAssets)
}

tasks.named("preBuild").configure {
    dependsOn(copyBootcampWeb)
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("androidx.webkit:webkit:1.11.0")
    implementation("androidx.activity:activity-ktx:1.9.2")
}
