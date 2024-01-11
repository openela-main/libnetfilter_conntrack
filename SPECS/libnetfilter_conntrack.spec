Name:           libnetfilter_conntrack
Version:        1.0.9
Release:        1%{?dist}
Summary:        Netfilter conntrack userspace library
License:        GPLv2+
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.bz2

Patch01:        0001-conntrack-fix-build-with-kernel-5.15-and-musl.patch
Patch02:        0002-expect-conntrack-Avoid-spurious-covscan-overrun-warn.patch

BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel >= 1.0.3
BuildRequires:  libnfnetlink-devel >= 1.0.1
BuildRequires:  make
BuildRequires:  pkgconfig

%description
libnetfilter_conntrack is a userspace library providing a programming 
interface (API) to the in-kernel connection tracking state table.

%package        devel
Summary:        Netfilter conntrack userspace library
Requires:       %{name} = %{version}-%{release}, libnfnetlink-devel >= 1.0.1
Requires:       kernel-headers

%description    devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%prep
%autosetup -p1

%build
%configure --disable-static --disable-rpath

%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_conntrack
%{_includedir}/libnetfilter_conntrack/*.h

%changelog
* Thu Dec 08 2022 Phil Sutter <psutter@redhat.com> - 1.0.9-1
- expect/conntrack: Avoid spurious covscan overrun warning
- conntrack: fix build with kernel 5.15 and musl
- New version 1.0.9

* Wed Dec 07 2022 Phil Sutter <psutter@redhat.com> - 1.0.8-5
- conntrack: don't cancel nest on unknown layer 4 protocols

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.8-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.8-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8
- Cleanup spec

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Paul Wouters <pwouters@redhat.com> - 1.0.7-1
- Updated to 1.0.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Paul Wouters <pwouters@redhat.com> - 1.0.6-1
- Updated to 1.0.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.4-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  8 2013 Paul P. Komkoff Jr <i@stingr.net> - 1.0.4-1
- new upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Paul P. Komkoff Jr <i@stingr.net> - 1.0.3-1
- new upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Paul P. Komkoff Jr <i@stingr.net> - 1.0.2-1
- new upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Paul P. Komkoff Jr <i@stingr.net> - 1.0.1-1
- new upstream version

* Sat Mar 17 2012 Paul P. Komkoff Jr <i@stingr.net> - 1.0.0-1
- new upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Apr  3 2011 Paul P. Komkoff Jr <i@stingr.net> - 0.9.1-1
- new upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.9.0-1
- new upstream version

* Wed Jan 20 2010 Paul P. Komkoff Jr <i@stingr.net> - 0.0.101-1
- new upstream version

* Mon Sep 28 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.0.100-1
- new upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.0.99-1
- new upstream version

* Sun Oct 26 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.97-1
- new upstream version

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.0.96-3
- Fix Patch0:/%%patch mismatch.

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.96-2
- fix license tag

* Wed Jul 16 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.96-1
- grab new upstream version
- use bundled header again

* Sat Feb 23 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.89-0.1.svn7356
- new version from upstream svn, with new api
- use system headers instead of bundled

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.82-3
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.82-2
- fix build with a new glibc

* Sun Jan 20 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.82-1
- new upstream version

* Thu Aug 30 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.81-1
- new upstream version

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.80-2
- Rebuild for selinux ppc32 issue.

* Thu Jul 19 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.80-1
- new upstream version

* Wed May 30 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.75-1
- new upstream version

* Sun Mar 25 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.50-4
- grab ownership of some directories

* Mon Mar 19 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.50-3
- include libnfnetlink-devel into -devel deps

* Sat Mar 17 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.50-2
- new way of handling rpaths (as in current packaging guidelines)

* Sun Feb 11 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.0.50-1
- upstream version 0.0.50

* Fri Sep 15 2006 Paul P. Komkoff Jr <i@stingr.net>
- rebuilt

* Wed Jul 12 2006 Felipe Kellermann <stdfk@terra.com.br> - 0.0.31-1
- Adds pkgconfig to devel files.
- Version 0.0.31.

* Mon May  8 2006 Paul P Komkoff Jr <i@stingr.net> - 0.0.30-2
- Include COPYING in %%doc

* Sun Mar 26 2006 Paul P Komkoff Jr <i@stingr.net> - 0.0.30-1
- Preparing for submission to fedora extras
