%define project_name imgproxy

Name: imgproxy
Version: 2.14.1
Release: stable
Summary: ImgProxy for centos7
License: MIT
URL: https://github.com/imgproxy/imgproxy/
Source0: imgproxy
BuildRoot: %{buildroot}
Requires: libexif
Requires: giflib
Requires: fftw
Requires: ImageMagick
BuildArch: x86_64
BuildRequires: systemd

%description
imgproxy is a fast and secure standalone server for resizing and converting remote images. The main principles of imgproxy are simplicity, speed, and security.

%install
rm -rf "%{buildroot}"

ls -lah %{_topdir}/SOURCES
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib64
cp %{_topdir}/SOURCES/imgproxy %{buildroot}/usr/bin/imgproxy
cp %{_topdir}/SOURCES/*so* %{buildroot}/usr/lib64
ls -lah %{buildroot}/usr/lib64
ls -lah %{buildroot}/usr/bin
mkdir -p "%{buildroot}/%{_unitdir}"
cp %{_topdir}/SOURCES/%{project_name}.service "%{buildroot}/%{_unitdir}"

%pre
getent group "%{project_name}" >/dev/null || groupadd -r "%{project_name}"
getent passwd "%{project_name}" >/dev/null || \
    useradd -r -g %{project_name} -d /bin/%{project_name} -s /sbin/nologin \
    -c "%{project_name} user" %{project_name}
exit 0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%systemd_post %{project_name}.service

%preun
%systemd_preun %{project_name}.service

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{project_name}
%{_libdir}/libvips.so.42
%{_libdir}/libwebp.so.7
%{_libdir}/libwebpmux.so.3
%{_libdir}/libwebpdemux.so.2
%{_libdir}/libopenslide.so.0
%{_libdir}/libhdf5.so.8
%{_libdir}/libmatio.so.9
%{_libdir}/libsz.so.2
%{_libdir}/libaec.so.0
%{_unitdir}/%{project_name}.service
