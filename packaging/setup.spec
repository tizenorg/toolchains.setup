Summary: A set of system configuration and setup files
Name: setup
Version: 0.2
Release: 1
License: Apache-2.0
Group: System/Base
URL: https://fedorahosted.org/setup/
Source0: https://fedorahosted.org/releases/s/e/%{name}/%{name}-0.1.tar.bz2
BuildArch: noarch
BuildRequires: bash
Requires: filesystem

%description
The setup package contains a set of important system configuration and
setup files, such as passwd, group, and profile.

%prep
%setup -q
./shadowconvert.sh

%build

%check
# Run any sanity checks.
#make check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/profile.d
cp -ar * %{buildroot}/etc
rm -f %{buildroot}/etc/uidgid
mkdir -p %{buildroot}/var/log
touch %{buildroot}/var/log/lastlog
touch %{buildroot}/etc/environment
chmod 0644 %{buildroot}/etc/environment
chmod 0400 %{buildroot}/etc/{shadow,gshadow}
chmod 0644 %{buildroot}/var/log/lastlog
touch %{buildroot}/etc/fstab
touch %{buildroot}/etc/mtab

# remove unpackaged files from the buildroot
rm -f %{buildroot}/etc/Makefile
rm -f %{buildroot}/etc/serviceslint
rm -f %{buildroot}/etc/uidgidlint
rm -f %{buildroot}/etc/shadowconvert.sh
rm -f %{buildroot}/etc/setup.spec
rm -rf %{buildroot}/etc/packaging

mkdir -p %{buildroot}/opt/etc
pushd %{buildroot}/etc
rm -f shadow gshadow
popd
mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
cp LICENSE.Apache-2.0 $RPM_BUILD_ROOT%{_datadir}/license/%{name}
rm -f $RPM_BUILD_ROOT/etc/LICENSE.Apache-2.0

%clean
rm -rf %{buildroot}

#throw away useless and dangerous update stuff until rpm will be able to
#handle it ( http://rpm.org/ticket/6 )
#%post -p <lua>
#for i, name in ipairs({"passwd", "shadow", "group", "gshadow"}) do
#     os.remove("/etc/"..name..".rpmnew")
#end

%files
%defattr(-,root,root,-)
%{_datadir}/license/setup
%verify(not md5 size mtime) %config(noreplace) /etc/passwd
%verify(not md5 size mtime) %config(noreplace) /etc/group
#/etc/shadow
#/etc/gshadow

%verify(not md5 size mtime) %config(noreplace) /etc/services
%verify(not md5 size mtime) %config(noreplace) /etc/exports
%config(noreplace) /etc/aliases
%config(noreplace) /etc/environment
%config(noreplace) /etc/filesystems
%config(noreplace) /etc/host.conf
%verify(not md5 size mtime) %config(noreplace) /etc/hosts
%verify(not md5 size mtime) %config(noreplace) /etc/hosts.allow
%verify(not md5 size mtime) %config(noreplace) /etc/hosts.deny
%verify(not md5 size mtime) %config(noreplace) /etc/motd
%config(noreplace) /etc/printcap
%verify(not md5 size mtime) %config(noreplace) /etc/inputrc
%config(noreplace) /etc/bashrc
%config(noreplace) /etc/profile
%verify(not md5 size mtime) %config(noreplace) /etc/protocols
%attr(0600,root,root) %config(noreplace,missingok) /etc/securetty
%config(noreplace) /etc/csh.login
%config(noreplace) /etc/csh.cshrc
%dir /etc/profile.d
%config(noreplace) %verify(not md5 size mtime) /etc/shells
%ghost %attr(0644,root,root) %verify(not md5 size mtime) /var/log/lastlog
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) /etc/fstab
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) /etc/mtab
%changelog
* Fri Mar 20 2015 WaLyong Cho <walyong.cho@samsung.com> - None
- PROJECT: external/setup
- COMMIT_ID: 7e34f70170d6e9384cff8dba5702b4f65e6d81bc
- BRANCH: master
- PATCHSET_REVISION: 7e34f70170d6e9384cff8dba5702b4f65e6d81bc
- CHANGE_OWNER: \"WaLyong Cho\" <walyong.cho@samsung.com>
- PATCHSET_UPLOADER: \"WaLyong Cho\" <walyong.cho@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/2529307
- PATCHSET_REVISION: 7e34f70170d6e9384cff8dba5702b4f65e6d81bc
- TAGGER: WaLyong Cho <walyong.cho@samsung.com>
- Gerrit patchset approval info:
- WaLyong Cho <walyong.cho@samsung.com> Verified : 1
- Kyungmin Park <kyungmin.park@samsung.com> Code-Review : 2
- Kyungmin Park <kyungmin.park@samsung.com> Verified : 1
- CHANGE_SUBJECT: Merge remote-tracking branch 'origin/devel/systemfw/master'
- Merge remote-tracking branch 'origin/devel/systemfw/master'
