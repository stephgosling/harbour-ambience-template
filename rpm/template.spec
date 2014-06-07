Name:       ambience-template

Summary:    Template ambience
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake

Requires:   ambienced

%description
This is a template ambience description

%package ts-devel
Summary:   Translation source for template ambience
License:   TBD
Group:     System/GUI/Other

%description ts-devel
Translation source for a template ambience

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_datadir}/ambience/ambience-template/ambience-template.ambience
%{_datadir}/ambience/ambience-template/sounds.index
%{_datadir}/ambience/ambience-template/images/*
%{_datadir}/ambience/ambience-template/sounds/*
%{_datadir}/translations/ambience-template_eng_en.qm

%files -n ambience-template-ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/ambience-template.ts
