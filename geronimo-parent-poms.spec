%global pkg_name geronimo-parent-poms
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:		%{?scl_prefix}%{pkg_name}
Version:	1.6
Release:	16.11%{?dist}
Summary:	Parent POM files for geronimo-specs
License:	ASL 2.0
URL:		http://geronimo.apache.org/
BuildArch:	noarch

# Following the parent chain all the way up ...
Source0:	http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:	%{?scl_prefix_java_common}javapackages-tools

# Dependencies and plugins from the POM files

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -c -T -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%pom_remove_parent
# IDEA plugin is not really useful in Fedora
%pom_remove_plugin :maven-idea-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_alias : org.apache.geronimo.specs:specs
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE


%changelog
* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 1.6-16.11
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.6-16.10
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.6-16.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.8
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.7
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.6
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-16.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.6-16
- Mass rebuild 2013-12-27

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-15
- Remove maven-idea-plugin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.6-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.6-12
- Build with xmvn

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-11
- Install LICENSE file
- Add missing R: jpackage-utils
- Update to current packaging guidelines

* Mon Aug  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-10
- Remove pom.xml from SCM

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Tomas Radej <tradej@redhat.com> - 1.6-8
- Removed maven-pmd-plugin R

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep  7 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-6
- Remove genesis poms from package (split into separate package)
- Use new macro for depmaps

* Thu May  5 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-5
- Add compatibility depmap for geronimo.specs:specs-parent
- Fixes according to new guidelines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  3 2010 Mary Ellen Foster <mefoster at gmail.com> 1.6-3
- Fix tabs and spaces in srpm
- Remove config flag from mavendepmapfragdir
- Add jpackage-utils to the BuildRequires

* Tue Jan 19 2010 Mary Ellen Foster <mefoster at gmail.com> 1.6-2
- Don't include the apache root pom; it's already in maven2-common-poms
- Double check the dependencies to include only what's in the POMs
- Add initial Provides for the genesis stuff
- Fix changelog

* Mon Jan 18 2010 Mary Ellen Foster <mefoster at gmail.com> 1.6-1
- Initial package
