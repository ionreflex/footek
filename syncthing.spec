Name:        syncthing
Version:    0.14.50
Release:    0%{?dist}
Summary:    Open, trustworthy and decentralized sync
# Set to amd64 or 386
%define arch    amd64

Group:        Applications/System
License:    MPLv2
URL:        https://github.com/syncthing/syncthing
Source0:    https://github.com/syncthing/syncthing/releases/download/v%{version}/syncthing-linux-%{arch}-v%{version}.tar.gz

Requires:    policycoreutils-python

%description
Syncthing replaces proprietary sync and cloud services with something open,
trustworthy and decentralized. Your data is your data alone and you deserve
to choose where it is stored, if it is shared with some third party and how
it's transmitted over the Internet.

%prep
tar -zxf %{SOURCE0}
cd syncthing-linux-%{arch}-v%{version}/

%install
mkdir -p %{buildroot}/usr/bin/
cd syncthing-linux-%{arch}-v%{version}/
cp syncthing %{buildroot}/usr/bin/

mkdir -p %{buildroot}/etc/systemd/system/
cp etc/linux-systemd/system/syncthing\@.service  %{buildroot}/etc/systemd/system/
cp etc/linux-systemd/system/syncthing-resume.service  %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/etc/systemd/user/
cp etc/linux-systemd/user/syncthing.service %{buildroot}/etc/systemd/user/


%files
%defattr(-,root,root)
/usr/bin/syncthing
/etc/systemd/system/syncthing@.service
/etc/systemd/system/syncthing-resume.service
/etc/systemd/user/syncthing.service

%changelog
* Tue Sep 25 2018 Dave Grenier <livegrenier@gmail.com>
- Bump synthing to version 0.14.50
