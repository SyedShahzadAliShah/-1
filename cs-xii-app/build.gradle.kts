plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.sindh.csxii.lectures"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.sindh.csxii.lectures"
        minSdk = 24
        targetSdk = 34
        versionCode = 2
        versionName = "1.0.1"
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
}

tasks.register<Copy>("syncWebAssets") {
    from("${rootProject.projectDir}/cs-xii-lecture-notes") {
        exclude("scripts/**", "README.md", "data/chapters_raw.json")
    }
    into("${projectDir}/src/main/assets/www")
}

tasks.named("preBuild") {
    dependsOn("syncWebAssets")
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.webkit:webkit:1.11.0")
}
