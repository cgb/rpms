# $Id$
# Authority: dag
# Upstream: Ash Berlin <ash$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-C3-Componentised

Summary: Perl module named Class-C3-Componentised
Name: perl-Class-C3-Componentised
Version: 1.0005
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-C3-Componentised/

Source: http://search.cpan.org/CPAN/authors/id/A/AS/ASH/Class-C3-Componentised-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Class-C3-Componentised is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Class::C3::Componentised.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/C3/
#%{perl_vendorlib}/Class/C3/Componentised/
%{perl_vendorlib}/Class/C3/Componentised.pm

%changelog
* Fri Apr 24 2009 Christoph Maser <cmr@financial.com> - 1.0005-1
- Updated to release 1.0005.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 1.0003-1
- Updated to release 1.0003.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 1.0001-1
- Initial package. (using DAR)
