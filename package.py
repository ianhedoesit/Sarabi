
from __future__ import print_function
from misc import YAMLFile

class FileList(dict):
  pass # Could be pulled from git, or get files and create? hmmm...

class PackageFile(YAMLFile):
  def set_defaults(self):
    self['name'] = ''
    self['description'] = ''
    self['repo'] = ''
    self['branch'] = 'master'
    self['files'] = []
    self['depends'] = []

class Package(dict):
  def __init__(self, name, catagory, version, remote):
    self['name'] = name
    self['catagory'] = catagory
    self['version'] = version
    self['remote'] = remote

  def get_atom(self, with_version=False):
    return '%s/%s%s::%s' % (self['catagory'], self['name'], '-' + self['version'] if with_version else '', self['remote']) 

  def valid_atom(self, atom):
    def compare(item):
      return (not atom[item]) or (self[item] == atom[item])
    return compare('name') and compare('catagory') and compare('version') and compare('remote')

  def update(self):
    # Update repo, create new filelist, compare and update
    pass

  def install(self):
    # Pull repo, get files, and create filelist
    # Could also look for user patches?
    pass

  def uninstall(self):
    # Check filelist, remove files, delete repo
    pass
