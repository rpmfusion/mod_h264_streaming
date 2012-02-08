Summary:	H264 streaming module for the Apache HTTP Server
Name:		mod_h264_streaming
Version:	2.2.7
Release:	2%{?dist}
Group:		System Environment/Daemons
License:	CC-BY-NC-SA
URL:		http://h264.code-shop.com/
Source0:	http://h264.code-shop.com/download/apache_%{name}-%{version}.tar.gz
Source1:	h264_streaming.conf
Patch:		mod_h264_streaming-2.2.7-httpd.patch
BuildRequires:	httpd-devel >= 2.0.39
Requires:	httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing httpd-devel)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

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
%patch -p1 -b .httpd

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# Install Apache configuration file
install -D -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/h264_streaming.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/%{name}.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/h264_streaming.conf

%changelog
* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Robert Scheck <robert@fedoraproject.org> 2.2.7-1
- Upgrade to 2.2.7
- Initial spec file for Fedora and Red Hat Enterprise Linux
