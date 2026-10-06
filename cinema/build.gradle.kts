plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.sindh.csteach"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.sindh.csteach"
        minSdk = 24
        targetSdk = 34
        versionCode = 2
        versionName = "1.1.0"
        ndk {
            abiFilters += listOf("arm64-v8a", "armeabi-v7a")
        }
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
    }

    packaging {
        jniLibs {
            pickFirsts += listOf("**/libc++_shared.so")
        }
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    implementation("androidx.webkit:webkit:1.11.0")
    implementation(files("libs/sherpa-onnx.aar"))
}

val generateScenes = tasks.register<Exec>("generateScenes") {
    workingDir(rootDir)
    commandLine("python3", "cinema/tools/build_scenes.py")
}

val fetchVoice = tasks.register<Exec>("fetchVoice") {
    workingDir(rootDir)
    commandLine("bash", "cinema/tools/fetch_voice.sh")
}

val fetchMathJax = tasks.register<Exec>("fetchMathJax") {
    workingDir(rootDir)
    commandLine("bash", "cinema/tools/fetch_mathjax.sh")
}

tasks.named("preBuild").configure {
    dependsOn(generateScenes, fetchVoice, fetchMathJax)
}
