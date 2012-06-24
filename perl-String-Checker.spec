#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Checker
Summary:	String::Checker - An extensible string validation module
Summary(pl):	String::Checker - rozszerzalny modu� sprawdzaj�cy poprawno�� �a�cuch�w
Name:		perl-String-Checker
Version:	0.03
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Date-Manip
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple library for checking a string against a given
set of expectations. It contains a number of pre-defined expectations
which can be used, and can also be extended to perform any arbitrary
match or modification on a string.

%description -l pl
To jest bardzo prosta biblioteka do sprawdzania �a�cucha pod k�tem
podanego zestawu oczekiwa�. Zawiera wiele predefiniowanych oczekiwa�,
kt�re mog� by� u�yte, a tak�e rozszerzone tak, aby przeprowadzi�
dowolne dopasowanie lub modyfikacj� �a�cucha.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
