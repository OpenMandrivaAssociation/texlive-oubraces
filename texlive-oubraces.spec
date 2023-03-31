Name:		texlive-oubraces
Version:	21833
Release:	2
Summary:	Braces over and under a formula
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oubraces
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a means to interleave \overbrace and \underbrace in
the same formula.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/oubraces/oubraces.sty
%doc %{_texmfdistdir}/doc/latex/oubraces/oubraces.pdf
%doc %{_texmfdistdir}/doc/latex/oubraces/oubraces.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
