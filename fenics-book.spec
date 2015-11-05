Name: fenics-book
Summary: A book about FEniCS project
Version: 20130430
Release: 1%{?dist}
License: FDL
URL: http://fenicsproject.org/
Source: %name-%version.tar.gz
Source1: http://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/emptypage/emptypage.sty
Source2: http://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/todonotes/todonotes.sty
#BuildArch: noarch
BuildPreReq: texlive-latex-recommended texlive-latex-extra
BuildPreReq: texlive-pictures /usr/bin/ps2pdf

%description
This is a FEniCS book. The book discuss the theoretical foundations for the
current components of FEniCS, function as a reference for users, and showcase
interesting applications built with FEniCS. The tentative title for the book is
Automated Scientific Computing.

It is also emphasized that chapters either discuss current FEniCS projects (in a
tutorial style), summarize (already published) theoretical results relevant for
the FEniCS software, or discuss the use of FEniCS in applications.

%prep
%setup

install -p -m644 %SOURCE1 %SOURCE2 packages

%build
%make_build final

%files
%doc book.pdf

%changelog
* Tue Nov 3 2015 Adrian Alves <alvesadrian@fedoraproject.org> 20130430-1
- Initial Build
