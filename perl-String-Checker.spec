#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Checker
Summary:	String::Checker - an extensible string validation module
Summary(pl.UTF-8):	String::Checker - rozszerzalny moduł sprawdzający poprawność łańcuchów
Name:		perl-String-Checker
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d7187638b490464c209f6d132450f0cb
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-Date-Manip}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple library for checking a string against a given
set of expectations. It contains a number of pre-defined expectations
which can be used, and can also be extended to perform any arbitrary
match or modification on a string.

%description -l pl.UTF-8
To jest bardzo prosta biblioteka do sprawdzania łańcucha pod kątem
podanego zestawu oczekiwań. Zawiera wiele predefiniowanych oczekiwań,
które mogą być użyte, a także rozszerzone tak, aby przeprowadzić
dowolne dopasowanie lub modyfikację łańcucha.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
