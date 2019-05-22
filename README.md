Steps to reproduce bug:

```console
$ git clone https://github.com/oliver-sanders/rose-app-upgrade-derived-opt-conf-bug.git rose-app-upgrade-bug
$ cd rose-app-upgrade-bug
$ rose app-upgrade -C myapp myapp2.0 -y
$ git diff
diff --git a/myapp/opt/rose-app-my-opt.conf b/myapp/opt/rose-app-my-opt.conf
index f2dee14..7173465 100644
--- a/myapp/opt/rose-app-my-opt.conf
+++ b/myapp/opt/rose-app-my-opt.conf
@@ -1,2 +1,5 @@
 [env]
 a=2
+
+[namelist:bar]
+bar=2
diff --git a/myapp/rose-app.conf b/myapp/rose-app.conf
index 6f5b285..3ac9dca 100644
--- a/myapp/rose-app.conf
+++ b/myapp/rose-app.conf
@@ -1,4 +1,10 @@
-meta=/home/h06/osanders/Documents/temptest/temp1/mymeta/myapp1.0
+meta=/home/h06/osanders/Documents/temptest/temp1/mymeta/myapp2.0
 
 [env]
 a=1
+
+[!!namelist:bar]
+bar=1
+
+[namelist:foo]
+foo=.false.
```

The inconsistency is that the upgrader creates `[namelist:bar]` as trigger
ignored in the base configuration but not in the optional configuration.

*myapp/rose-app.conf*
```ini
[!!namelist:bar]
```

*myapp/opt/rose-app-my-opt.conf*
```ini
[namelist:bar]
```
