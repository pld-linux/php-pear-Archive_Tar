%include	/usr/lib/rpm/macros.php
%define		_class		Archive
%define		_subclass	Tar
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Tar file management class
Summary(pl):	%{_class}_%{_subclass} - klasa do zarz±dzania plikami Tar
Name:		php-pear-%{_pearname}
Version:	0.9
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of tar files in PHP. It supports
creating, listing, extracting and adding to tar files. Gzip support is
available if PHP has the zlib extension built-in or loaded.

%description -l pl
Ta klasa udostêpnia obs³ugê plików tar w PHP. Pozwala na tworzenie,
przegl±danie zawarto¶ci, rozpakowywanie i dodawanie plików do archiwów
tar. Obs³uga kompresji gzip jest dostêpna, je¶li do PHP jest
zainstalowany modu³ rozszerzenia zlib.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_class}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
