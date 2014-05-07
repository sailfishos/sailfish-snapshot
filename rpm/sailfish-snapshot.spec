%define package_summary Snapshot and factory image tool
%define version_info %{version}-%{release}

Name:          sailfish-snapshot
Version:       1.0
Release:       1
Summary:       %{package_summary}
Group:         System/Base
License:       ISC
Source0:       %{name}-%{version}.tar.gz
Requires:      btrfs-progs
Requires:      util-linux
Requires:      coreutils
Requires:      tar
BuildArch:     noarch

%description
%{summary}.

%prep
%setup -q

%build
make PREFIX=%{_prefix} VERSION=%{version_info}

%install
make install PREFIX=%{_prefix} VERSION=%{version_info} DESTDIR=%{buildroot}

%files
%attr(755,root,root) %{_bindir}/%{name}
%attr(644,root,root) %{_datadir}/%{name}/mountpoint.conf

%package sbj-config
Summary: %{package_summary} (SbJ configuration)
Requires: %{name} = %{version}

%description sbj-config
%{summary}.

%files sbj-config
%attr(644,root,root) %{_datadir}/%{name}/partition-sbj.conf
