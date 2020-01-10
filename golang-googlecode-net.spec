%global debug_package   %{nil}
%global import_path     code.google.com/p/go.net
%global gopath          %{_datadir}/gocode
%global rev             84a4013f96e01fdd14b65d260a78b543e3702ee1
%global shortrev        %(r=%{rev}; echo ${r:0:12})

Name:           golang-googlecode-net
Version:        0
Release:        0.12.hg%{shortrev}%{?dist}
Summary:        Supplementary Go networking libraries
License:        BSD
URL:            http://%{import_path}
Source0:        https://net.go.googlecode.com/archive/%{rev}.zip
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
Requires:       golang
Summary:        Supplementary Go networking libraries
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/dict) = %{version}-%{release}
Provides:       golang(%{import_path}/html) = %{version}-%{release}
Provides:       golang(%{import_path}/html/atom) = %{version}-%{release}
Provides:       golang(%{import_path}/idna) = %{version}-%{release}
Provides:       golang(%{import_path}/ipv4) = %{version}-%{release}
Provides:       golang(%{import_path}/ipv6) = %{version}-%{release}
Provides:       golang(%{import_path}/proxy) = %{version}-%{release}
Provides:       golang(%{import_path}/publicsuffix) = %{version}-%{release}
Provides:       golang(%{import_path}/spdy) = %{version}-%{release}
Provides:       golang(%{import_path}/websocket) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go networking libraries.


%prep

%setup -n net.go-%{shortrev}
cp html/testdata/webkit/README README-webkit

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in dict html idna ipv4 ipv6 proxy publicsuffix spdy websocket; do
   cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%doc README-webkit
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/code.google.com
%dir %attr(755,root,root) %{gopath}/src/code.google.com/p
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/dict
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/html
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/html/atom
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/html/testdata
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/html/testdata/webkit
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/html/testdata/webkit/scripted
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/idna
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/ipv4
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/ipv6
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/proxy
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/publicsuffix
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/spdy
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/websocket
%{gopath}/src/%{import_path}/dict/*.go
%{gopath}/src/%{import_path}/html/*.go
%{gopath}/src/%{import_path}/html/atom/*.go
%{gopath}/src/%{import_path}/html/testdata/*.html
%{gopath}/src/%{import_path}/html/testdata/webkit/*.dat
%{gopath}/src/%{import_path}/html/testdata/webkit/README
%{gopath}/src/%{import_path}/html/testdata/webkit/scripted/*.dat
%{gopath}/src/%{import_path}/idna/*.go
%{gopath}/src/%{import_path}/ipv4/*.go
%{gopath}/src/%{import_path}/ipv6/*.go
%{gopath}/src/%{import_path}/proxy/*.go
%{gopath}/src/%{import_path}/publicsuffix/*.go
%{gopath}/src/%{import_path}/spdy/*.go
%{gopath}/src/%{import_path}/websocket/*.go

%changelog
* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.hg84a4013f96e0
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.11.hg84a4013f96e0
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.10.hg84a4013f96e0
- removed double quotes from Provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.hg84a4013f96e0
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.hg84a4013f96e0
- exclusivearch as per golang package
- debug_package nil

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.7.hg
- install just the source code for devel package

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.6.hg
- All Provides listed explicitly

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg
- Provides corrected

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg
- comment cleanup
- build explanation

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg
- html/webkit/scripted ownership set
- codereview.cfg not packaged

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg
- IPv6 doesn't build
- Typo correction
- directory ownership taken care of

* Thu Sep 19 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg
- Initial fedora package
