Summary:	Simple bootloader
Summary(pl):	Prosty bootloader
Summary(pt_BR):	Carregador de boot simples
Summary(zh_CN):	Linux²Ù×÷ÏµÍ³µÄÆô¶¯¹ÜÀíÆ÷
Name:		syslinux
Version:	2.05
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	dc68729fa6a39e6f630cf8643b19eab4
Patch0:		%{name}-nowin32.patch
Patch1:		%{name}-cpp-comment.patch
URL:		http://syslinux.zytor.com/
BuildRequires:	perl
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SYSLINUX is a boot loader for the Linux operating system which
operates off MS-DOS floppies. It is intended to simplify first-time
installation of Linux, rescue disks, and other uses for boot floppies.
A SYSLINUX floppy can be manipulated using standard MS-DOS (or any
other OS that can access an MS-DOS filesystem) tools once it has been
created, and requires only a ~ 7K DOS program or ~ 13K Linux program
to create it in the first place. It also includes PXELINUX, a program
to boot off a network server using a boot PROM compatible with the
Intel PXE (Pre-Execution Environment) specification.

%description -l pl
SYSLINUX jest boot-loaderem dla Linux'a, który operuje na dyskietkach
z systemem plików MS-DOS. Jego przeznaczeniem jest uproszczenie
pierwszej instalacji Linux'a, dyskietki ratunkowe oraz inne rzeczy
zwi±zane z dyskietkami. Dyskietka SYSLINX'owa mo¿e byæ modyfikowana w
systemie MS-DOS (a tak¿e ka¿dym innym systemie z dostêpem do systemu
plików MS-DOS) gdy narzêdzia sa ju¿ stworzone, a tak¿e potrzebuje
tylko ~7K programu DOS'owego lub ~13K programu Linux'owego do
stworzenia ich po raz pierwszy. Zawiera tak¿e program PXELINUX -
program s³u¿±cy do bootowania servera sieciowego poprzez Boot-PROM
kompatybilny ze specyfikacj± Intel PXE (Pre-Execution Environment).

%description -l pt_BR
SYSLINUX é um carregador de boot para o linux, operando em disquetes
com formatação DOS. Sua intenção é simplificar instalações do Linux,
discos de recuperação, e outros usos para disquetes de boot. Um
disquete SYSLINUX pode ser manipulado usando ferramentas padrão do DOS
(ou qualquer sistema que possa acessar um filesystem DOS) e requer
somente um programa DOS de aproximadamente 7K ou linux de 13K para
criá-lo na primeira vez.

Também inclui o PXELINUX, um programa para boot remoto a partir de um
servidor de rede usando um boot PROM compatível com a especificação
Intel PXE (Pre-Execution Environment).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CC=%{__cc}
%{__make} -C memdisk CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}

install *.sys *.bin *.com pxelinux.0 $RPM_BUILD_ROOT%{_libdir}/%{name}
install memdisk/memdisk $RPM_BUILD_ROOT%{_libdir}/%{name}
install syslinux $RPM_BUILD_ROOT%{_bindir}

# I'm not sure if this should be packed /klakier
#install gethostip $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.doc */*.doc
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
