%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}

# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:     %{expand: %%global _httpd_moddir     %%{_libdir}/httpd/modules}}

Summary:	H264 streaming module for the Apache HTTP Server
Name:		mod_h264_streaming
Version:	2.2.7
Release:	21%{?dist}
Group:		System Environment/Daemons
License:	CC-BY-NC-SA
URL:		https://github.com/code-shop-com/h264
Source0:	http://h264.code-shop.com/download/apache_%{name}-%{version}.tar.gz
Source1:	h264_streaming.conf
Patch0:	mod_h264_streaming-2.2.7-httpd.patch
BuildRequires:  gcc-c++
BuildRequires:	httpd-devel >= 2.0.39
Requires:	httpd-mmn = %{_httpd_mmn}

%description
H264 streaming module enable viewers to immediately jump to any part of
the video regardless of the length of the video or whether it has all
been downloaded yet. It also supports 'virtual video clips', so it can
be specified to only playback a part of the video or create download
links to specific parts of the video. If the video is already using the
widely adopted MPEG4/H264 industry standard, there's no need to recode
MP4 videos, the existing video files can be used.

This version is free if you agree to the noncommercial license. Please
mention its use on your website, in the lines of 'This website uses H264
pseudo video streaming technology by CodeShop'. The commercial license
is inexpensive, see the following link if you need a commercial license:
http://h264.code-shop.com/trac/wiki/Mod-H264-Streaming-License-Version2

%prep
%setup -q
%patch -P0 -p1 -b .httpd

%build
%configure
%make_build

%install
%make_install

# Install Apache configuration file
%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# httpd <= 2.2.x
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/h264_streaming.conf
%else
# httpd >= 2.4.x
head -n 5 %{SOURCE1} > 10-h264_streaming.conf
sed -e '4,5d' %{SOURCE1} > h264_streaming.conf
touch -c -r %{SOURCE1} 10-h264_streaming.conf h264_streaming.conf
install -D -p -m 644 10-h264_streaming.conf $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-h264_streaming.conf
install -D -p -m 644 h264_streaming.conf $RPM_BUILD_ROOT%{_httpd_confdir}/h264_streaming.conf
%endif

%files
%{_httpd_moddir}/%{name}.so
%config(noreplace) %{_httpd_confdir}/h264_streaming.conf
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %{_httpd_modconfdir}/10-h264_streaming.conf
%endif

%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild
- Fix build and some cleanups

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.7-9
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 2.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 03 2014 Sérgio Basto <sergio@serjux.com> - 2.2.7-4
- Rebuild to match with Apache 2.4 version.
- Update httpd_mmn detection copied from mod_security.spec 

* Sat Nov 17 2012 Robert Scheck <robert@fedoraproject.org> 2.2.7-3
- Updated spec file to match with Apache 2.4 policy

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Robert Scheck <robert@fedoraproject.org> 2.2.7-1
- Upgrade to 2.2.7
- Initial spec file for Fedora and Red Hat Enterprise Linux
