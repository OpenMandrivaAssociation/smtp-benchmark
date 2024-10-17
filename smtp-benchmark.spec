Summary:	SMTP Benchmark Suite
Name:		smtp-benchmark
Version:	1.0.3
Release:	9
License:	BSD
Group:		Networking/Other
URL:		https://www.etc.msys.ch/software/smtp-benchmark/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		smtp-benchmark-linux_fix.diff
BuildRoot:	%{_tmppath}/%{name}-root

%description
smtp-benchmark consists of two programs, smtpsend and smtpsink.
Whereas smtpsend is used to send generated e-mail messages using
SMTP to a mail transfer agent, smtpsink is designed to dispose of
received messages as quick as possible.

smtpsend measures the time spent sending e-mails and the number
of e-mails actually sent and outputs statistics after the program
run.

smtpsend can fork one or more parallel senders each using one or
more sequential connections to a SMTP server to deliver one or
more messages per connection.

smtpsink comes in handy when the relaying performance of a MTA is
to be measured.

%prep

%setup -q -n %{name}
%patch0 -p0

%build

gcc %{optflags} -o smtpsend/smtpsend smtpsend/smtpsend.c
gcc %{optflags} -o smtpsink/smtpsink smtpsink/smtpsink.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -m0755 smtpsend/smtpsend %{buildroot}%{_sbindir}/
install -m0755 smtpsink/smtpsink %{buildroot}%{_sbindir}/
install -m0644 smtpsend/smtpsend.8 %{buildroot}%{_mandir}/man8/
install -m0644 smtpsink/smtpsink.8 %{buildroot}%{_mandir}/man8/
  
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc README
%{_sbindir}/smtpsend
%{_sbindir}/smtpsink
%{_mandir}/man8/smtpsend.8*
%{_mandir}/man8/smtpsink.8*




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-8mdv2010.0
+ Revision: 433966
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-7mdv2009.0
+ Revision: 260858
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-6mdv2009.0
+ Revision: 252653
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.3-4mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdv2007.0
+ Revision: 131208
- Import smtp-benchmark

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-3mdk
- rebuild

* Sat Jan 01 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.3-2mdk
- rebuild (1.0.4 won't build)

