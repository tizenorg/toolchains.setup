Name:           setup
Version:        0.5
Release:        1
License:        Public Domain
Summary:        A set of system configuration and setup files
Url:            https://fedorahosted.org/setup/
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
Source1001:     packaging/setup.manifest
BuildRequires:  bash
BuildArch:      noarch
Requires(pre): filesystem

%description
The setup package contains a set of important system configuration and
setup files, such as passwd, group, and profile.

%prep
%setup -q

./shadowconvert.sh

%build
cp %{SOURCE1001} .

%check
# Run any sanity checks.
make check

%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cp -ar * %{buildroot}/etc
rm -f %{buildroot}%{_sysconfdir}/uidgid
rm -f %{buildroot}%{_sysconfdir}/COPYING
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/lastlog
touch %{buildroot}%{_sysconfdir}/environment
chmod 0644 %{buildroot}%{_sysconfdir}/environment
chmod 0400 %{buildroot}%{_sysconfdir}/{shadow,gshadow}
chmod 0644 %{buildroot}%{_localstatedir}/log/lastlog
touch %{buildroot}%{_sysconfdir}/fstab
touch %{buildroot}%{_sysconfdir}/mtab

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_sysconfdir}/Makefile
rm -f %{buildroot}%{_sysconfdir}/serviceslint
rm -f %{buildroot}%{_sysconfdir}/uidgidlint
rm -f %{buildroot}%{_sysconfdir}/shadowconvert.sh
rm -rf %{buildroot}%{_sysconfdir}/packaging
rm -rf %{buildroot}%{_sysconfdir}/*.manifest


#throw away useless and dangerous update stuff until rpm will be able to
#handle it ( http://rpm.org/ticket/6 )
%post -p <lua>
for i, name in ipairs({"passwd", "shadow", "group", "gshadow"}) do
     os.remove("/etc/"..name..".rpmnew")
end

%files
%manifest setup.manifest
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/passwd
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/group
%verify(not md5 size mtime) %attr(0000,root,root) %config(noreplace,missingok) %{_sysconfdir}/shadow
%verify(not md5 size mtime) %attr(0000,root,root) %config(noreplace,missingok) %{_sysconfdir}/gshadow
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/services
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/exports
%config(noreplace) %{_sysconfdir}/aliases
%config(noreplace) %{_sysconfdir}/environment
%config(noreplace) %{_sysconfdir}/filesystems
%config(noreplace) %{_sysconfdir}/host.conf
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts.allow
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts.deny
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/motd
%config(noreplace) %{_sysconfdir}/printcap
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/inputrc
%config(noreplace) %{_sysconfdir}/bashrc
%config(noreplace) %{_sysconfdir}/profile
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/protocols
%attr(0600,root,root) %config(noreplace,missingok) %{_sysconfdir}/securetty
%config(noreplace) %{_sysconfdir}/csh.login
%config(noreplace) %{_sysconfdir}/csh.cshrc
%dir %{_sysconfdir}/profile.d
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/shells
%ghost %attr(0644,root,root) %verify(not md5 size mtime) %{_localstatedir}/log/lastlog
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) %{_sysconfdir}/fstab
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) %{_sysconfdir}/mtab
