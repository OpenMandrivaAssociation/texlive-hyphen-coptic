Name:		texlive-hyphen-coptic
Version:	73410
Release:	1
Summary:	Coptic hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-coptic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Coptic in UTF-8 encoding as well as in
ASCII-based encoding for 8-bit engines. The latter can only be
used with special Coptic fonts (like CBcoptic). The patterns
are considered experimental.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-coptic
%_texmf_language_def_d/hyphen-coptic
%_texmf_language_lua_d/hyphen-coptic
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-coptic <<EOF
\%% from hyphen-coptic:
coptic loadhyph-cop.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-coptic
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-coptic <<EOF
\%% from hyphen-coptic:
\addlanguage{coptic}{loadhyph-cop.tex}{}{1}{1}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-coptic
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-coptic <<EOF
-- from hyphen-coptic:
	['coptic'] = {
		loader = 'loadhyph-cop.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-cop.pat.txt',
		hyphenation = '',
	},
EOF
