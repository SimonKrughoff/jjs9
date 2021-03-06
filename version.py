"""jjs9 version"""
#import git
#repo = git.Repo(search_parent_directories=True)
#dev = repo.active_branch.name + '-' + repo.head.commit.hexsha[0:7]
dev = 'dev'

version_tag = (1, 0, 0, dev)
__version__ = '.'.join(map(str, version_tag[:3]))

if len(version_tag) > 3:
    __version__ = '%s-%s' % (__version__, version_tag[3])
