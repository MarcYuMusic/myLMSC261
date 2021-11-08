# Error Log
While my path to getting this DAMN THING TO WORK is quite straitforward, it was frankly just...lots of waiting around. When I tried to download Homebrew, I was hit with this error:

```
Error: No similarly named formulae found.
Error: No previously deleted formula found.
Error: No formulae found in taps.
```

Apparently, I had another version of Homebrew already installed. So all I had to do was update Homebrew. I began updating Homebrew, but because it took awhile, I detoured and tried restarting it several times until I found out that...that is bad. So I let it sit there...and then it updated. Then I proceeded to download install libraries for Pyo (libsndfile, portaudio, portmidi, and liblo), all of which worked except for portmidi. And that's where my progress in class stopped! This is the end of the captain's log—until the next time I spend an hour figuring out how to get these files to work.

A week later, I return this assignment to download portaudio.

```
==> Downloading https://github.com/Kitware/CMake/releases/download/v3.21.4/cmake
Already downloaded: /Users/marcyu/Library/Caches/Homebrew/downloads/ad01c4a15a1e9fab7a8eba5abd0eeaf1277f7a38d2a1db585e14f573199b1a86--cmake-3.21.4.tar.gz
==> Downloading https://sources.debian.org/data/main/p/portmidi/1:217-6/debian/p
Already downloaded: /Users/marcyu/Library/Caches/Homebrew/downloads/b88f1c1d6fe01452a01766749a82a562a5890ee4f3366ad675036d2923d04b88--13-disablejni.patch
==> Downloading https://downloads.sourceforge.net/project/portmedia/portmidi/217
Already downloaded: /Users/marcyu/Library/Caches/Homebrew/downloads/db61c8c52cb79ff9f70f85a27306df48988e77f9e526a612c421074e6775bc5e--portmidi-src-217.zip
==> Installing dependencies for portmidi: cmake
==> Installing portmidi dependency: cmake
==> ./bootstrap --prefix=/usr/local/Cellar/cmake/3.21.4 --no-system-libs --paral
```

I've been sitting here for at least 10 minutes now. Then I press Enter, and it continues:

```
==> make
```

It stalls again...and 10 minutes later, it continues the next line. So I don't know if pressing Enter earlier really did anything. And unfortunately...there have been too many fatal errors:

```
fatal error: too many errors emitted, stopping now [-ferror-limit=]
//Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/System/Library/Frameworks/Carbon.framework/Frameworks/Ink.framework/Headers/Ink.h:776:63: error: expected function body after function declarator
InkUserWritingMode(void)                                      AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_14;
                                                              ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 error20 errors generated.
s generated.
make[3]: *** [pm_common/CMakeFiles/portmidi-static.dir/__/pm_mac/readbinaryplist.c.o] Error 1
make[3]: *** [pm_dylib/CMakeFiles/portmidi-dynamic.dir/__/pm_mac/readbinaryplist.c.o] Error 1
make[2]: *** [pm_dylib/CMakeFiles/portmidi-dynamic.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[2]: *** [pm_common/CMakeFiles/portmidi-static.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [all] Error 2

Do not report this issue to Homebrew/brew or Homebrew/core!


Error: You are using macOS 10.13.
We (and Apple) do not provide support for this old version.
You will encounter build failures with some formulae.
Please create pull requests instead of asking for help on Homebrew's GitHub,
Twitter or any other official channels. You are responsible for resolving
any issues you experience while you are running this
old version
```

It appears that the issue may be that my macOS is not the right version. However, due to whatever softwares I have here, I'm hesitant to update my computer, so this is where my progress stops for today. I've tried running this code:

```
sudo python3 setup.py install --use-coreaudio --debug
```

...but it gives me fatal error: 'portmidi.h' not found. I do not believe I can progress past this point without updating my computer as the next logical step.