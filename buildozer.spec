[app]
title = Floating Ball
package.name = floatingball
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1
requirements = python3,kivy

orientation = portrait

# Permissions needed for floating overlay
android.permissions = SYSTEM_ALERT_WINDOW

# Android specific
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.gradle_dependencies = ''

# Kivy launcher
fullscreen = 0

[buildozer]
log_level = 2