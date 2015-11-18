Name: make-initrd-busybox
Version: 1.24.1
Release: alt1

Summary: Busybox for make-initrd
License: GPL
Group: System/Base

Source0: %name-%version.tar

# For new put-file utility
Requires: make-initrd >= 0.8.2-alt1

%description
Busybox (%version) for make-initrd.

%prep
%setup
cp -f -- busybox-config busybox/.config

%build
cd busybox
%make_build

%install
mkdir -p -- %buildroot/lib/initrd/var/run

cd busybox
%make install CONFIG_PREFIX=%buildroot/lib/initrd

cd %buildroot/lib/initrd

ln -s ../usr/bin/readlink bin/readlink
ln -s ../usr/sbin/chroot  sbin/chroot

%files 
/lib/initrd/*

%changelog
* Wed Nov 18 2015 Alexey Gladkov <legion@altlinux.ru> 1.24.1-alt1
- New busybox version (1.24.1).

* Fri Jul 04 2014 Alexey Gladkov <legion@altlinux.ru> 0.2-alt1
- Add more utilities.

* Wed Mar 13 2013 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial.

