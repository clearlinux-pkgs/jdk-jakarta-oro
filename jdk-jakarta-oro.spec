Name     : jdk-jakarta-oro
Version  : 2.0.8
Release  : 2
URL      : http://archive.apache.org/dist/jakarta/oro/jakarta-oro-2.0.8.tar.gz
Source0  : http://archive.apache.org/dist/jakarta/oro/jakarta-oro-2.0.8.tar.gz
Source1  : http://repo1.maven.org/maven2/oro/oro/2.0.8/oro-2.0.8.pom
Source2  : MANIFEST.MF
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1
BuildRequires : apache-maven
BuildRequires : apache-ant
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch0   : jakarta-oro-build-xml.patch

%description
Quick Overview
--------------
CHANGES - lists recent changes to the source code
COMPILE - contains quick instructions for building the library
CONTRIBUTORS - lists people who have contributed to developing the code
ISSUES  - contains a list of known bugs
KEYS    - lists PGP keys used to sign releases
LICENSE - the license defining the terms of use of the software
STYLE   - a set of guidelines for developers of the code
TODO    - lists planned or possible changes/additions

%prep
%setup -q -n jakarta-oro-2.0.8
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# remove all CVS files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done

%patch0
mv %{SOURCE2} .

%build
ant -Dfinal.name=oro jar javadocs

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jakarta-oro.pom
cp oro.jar %{buildroot}/usr/share/java/jakarta-oro.jar
pushd %{buildroot}/usr/share/java/
ln -sf jakarta-oro.jar oro.jar
popd

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/jakarta-oro.xml \
%{buildroot}/usr/share/maven-poms/jakarta-oro.pom \
%{buildroot}/usr/share/java/jakarta-oro.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/jakarta-oro.jar
/usr/share/java/oro.jar
/usr/share/maven-metadata/jakarta-oro.xml
/usr/share/maven-poms/jakarta-oro.pom
