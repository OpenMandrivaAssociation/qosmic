%define name	qosmic
%define version	1.4.4
%define release	%mkrel 1

Summary:	Graphical interface for creating flam3 fractal images
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Graphics
Url:		http://code.google.com/p/qosmic/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	flam3-devel, lua-devel, libxml2-devel
BuildRequires:	jpeg-devel, qt4-devel

%description
Qosmic is graphical interface for creating, editing, and rendering
flam3 fractal images. The electricsheep screen saver has been gaining
popularity, and Qosmic was developed to provide a Qt interface for
people interested in creating and contributing sheep.

%prep
%setup -q -n %{name}

%build
qmake
%make

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_bindir}
%__chmod 755 %{buildroot}%{_bindir}
%__install -m 755 ./qosmic %{buildroot}%{_bindir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* changes.txt COPYING
%_bindir/*

