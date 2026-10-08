plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.teachyourself.sketchnotes"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.teachyourself.sketchnotes"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
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
        buildConfig = true
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.webkit:webkit:1.11.0")
}

val fetchMathJax = tasks.register<Exec>("fetchMathJax") {
    workingDir(rootDir)
    commandLine("bash", "tools/fetch_mathjax.sh")
}

val buildContent = tasks.register<Exec>("buildContent") {
    workingDir(rootDir)
    commandLine("python3", "tools/build_content.py")
}

tasks.named("preBuild").configure {
    dependsOn(fetchMathJax, buildContent)
}

tasks.register<Copy>("copyDebugApk") {
    from(layout.buildDirectory.file("outputs/apk/debug/app-debug.apk"))
    into(rootProject.file("releases"))
    rename { "TeachYourselfSketchnotes-v${android.defaultConfig.versionName}-debug.apk" }
}

afterEvaluate {
    tasks.named("assembleDebug").configure {
        finalizedBy("copyDebugApk")
    }
}
