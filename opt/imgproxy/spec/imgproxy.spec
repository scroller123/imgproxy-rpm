Name: imgproxy
Version: 2.14.1
Release: stable
Summary: ImgProxy for centos7
License: MIT
URL: https://github.com/imgproxy/imgproxy/
Source0: imgproxy
BuildRoot: %{_tmppath}/%{name}-for-%{version}-%{release}
Requires: libexif
Requires: matio
Requires: giflib
Requires: fftw
Requires: ImageMagick
BuildArch: x86_64

%define major 2

%description
imgproxy is a fast and secure standalone server for resizing and converting remote images. The main principles of imgproxy are simplicity, speed, and security.

%install
ls -lah %{_topdir}/SOURCES
ls -lah %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib64
cp %{_topdir}/SOURCES/imgproxy %{buildroot}/usr/bin/imgproxy
cp %{_topdir}/SOURCES/*so* %{buildroot}/usr/lib64
ls -lah %{buildroot}/usr/lib64
ls -lah %{buildroot}/usr/bin




%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/imgproxy
%{_libdir}/libvips.so.42
%{_libdir}/libwebp.so.7
%{_libdir}/libwebpmux.so.3
%{_libdir}/libwebpdemux.so.2
