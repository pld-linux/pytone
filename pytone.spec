Summary:	PyTone is a music jukebox
Summary(hu.UTF-8):	PyTone egy zenelejátszó
Name:		pytone
Version:	3.0.2
Release:	0.1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.luga.de/pytone/download/PyTone-%{version}.tar.gz
# Source0-md5:	f9560c571df84ad9c83c3a113882bb81
URL:		http://www.luga.de/pytone/
BuildRequires:	libao-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-mad
Requires:	python-pyao
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyTone is a music jukebox written in Python with a curses based GUI.
While providing advanced features like crossfading and multiple
players, special emphasis is put on ease of use, turning PyTone into
an ideal jukebox system for use at parties.

%description -l hu.UTF-8
PyTone egy Python-ban írt zenelejátszó curses-alapú GUI-val. Mivel
haladó lehetőségeket is tartalmaz, mint az átmenet és több lejátszó,
különös tekintettel a könnyű használatra, a PyTone egy ideális
lejátszó rendszer lehet különböző partikon.

%prep
%setup -q -n PyTone-%{version}
sed -i "2 s@src@%{py_sitedir}/%{name}@" pytone pytonectl

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install conf/{layout.compact,layout.ultracompact,pytonerc} $RPM_BUILD_ROOT%{_sysconfdir}

%find_lang PyTone

%clean
rm -rf $RPM_BUILD_ROOT

%files -f PyTone.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/pytone*
%{py_sitedir}/PyTone*egg-info
%{py_sitedir}/pytone
