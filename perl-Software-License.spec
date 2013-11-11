%define upstream_name    Software-License
%define upstream_version 0.103007

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
BuildArch:  noarch

Summary:	Packages that provide templated software licenses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Software-License-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(Data::Section)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Text::Template)

%description
This packages provides templated software licenses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Software

%changelog
* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.340-1mdv2011.0
+ Revision: 572708
- update to 0.102340

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.102.250-1mdv2011.0
+ Revision: 569956
- update to 0.102250

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.620-1mdv2011.0
+ Revision: 552632
- update to 0.101620

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.15.0-2mdv2010.1
+ Revision: 528119
- rebuild
- update to 0.015

* Tue Mar 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.14.0-1mdv2010.1
+ Revision: 526890
- update to 0.014

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.13.0-1mdv2010.1
+ Revision: 526456
- update to 0.013

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.012-1mdv2010.0
+ Revision: 384031
- update to new version 0.012

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.010-1mdv2010.0
+ Revision: 376721
- new version

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.008-1mdv2009.1
+ Revision: 300701
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.004-2mdv2009.0
+ Revision: 268723
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.004-1mdv2009.0
+ Revision: 195164
- import perl-Software-License


* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.004-1mdv2009.0
- first mdv release

