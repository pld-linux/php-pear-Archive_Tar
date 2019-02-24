#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build without PEAR installed (for first php-pear-PEAR installation)

%define		status		stable
%define		pearname	Archive_Tar
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Tar file management class
Summary(pl.UTF-8):	%{pearname} - klasa do zarządzania plikami Tar
Name:		php-pear-%{pearname}
Version:	1.4.5
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	86f50dd602f23d1dc4e1d983a584cd38
URL:		http://pear.php.net/package/Archive_Tar/
%if %{without bootstrap}
BuildRequires:	php-pear-PEAR
%endif
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of tar files in PHP. It supports
creating, listing, extracting and adding to tar files. Gzip support is
available if PHP has the zlib extension built-in or loaded.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta klasa udostępnia obsługę plików tar w PHP. Pozwala na tworzenie,
przeglądanie zawartości, rozpakowywanie i dodawanie plików do archiwów
tar. Obsługa kompresji gzip jest dostępna, jeśli do PHP jest
zainstalowany moduł rozszerzenia zlib.

Ta klasa ma w PEAR status: %{status}.

%prep
%if %{without bootstrap}
%pear_package_setup
%else
%setup -q -c -n %{pearname}-%{version}
%{__mv} %{pearname}-%{version}/* .
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}

%if %{without bootstrap}
%pear_package_install
%else
cp -pr Archive $RPM_BUILD_ROOT%{php_pear_dir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{without bootstrap}
%doc install.log docs/%{pearname}/docs/*
%{php_pear_dir}/.registry/archive_tar.reg
%endif
%{php_pear_dir}/Archive/Tar.php
