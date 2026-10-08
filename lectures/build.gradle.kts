plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.sindhcs.lectures"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.sindhcs.lectures"
        minSdk = 24
        targetSdk = 34
        versionCode = 8
        versionName = "2.2.0"
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

    buildFeatures {
        viewBinding = true
        buildConfig = true
    }

    androidResources {
        noCompress += "flv"
    }
}

tasks.register<Exec>("exportLectureAssets") {
    workingDir = rootProject.projectDir
    commandLine("python3", "scripts/export_lecture_catalog.py")
}

tasks.register<Exec>("exportLectureFlv") {
    workingDir = rootProject.projectDir
    commandLine("python3", "scripts/export_lecture_flv.py")
    dependsOn("exportLectureAssets")
}

tasks.named("preBuild") {
    dependsOn("exportLectureFlv")
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    implementation("androidx.recyclerview:recyclerview:1.3.2")
    implementation("androidx.cardview:cardview:1.0.0")
    implementation("androidx.media3:media3-exoplayer:1.4.1")
    implementation("androidx.media3:media3-ui:1.4.1")
}
