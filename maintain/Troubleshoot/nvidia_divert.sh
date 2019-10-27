LC_MESSAGES=C dpkg-divert --list '*nvidia-340*' | sed -nre 's/^diversion of (.*) to .*/\1/p' | xargs -rd'
' -n1 -- sudo dpkg-divert --remove
