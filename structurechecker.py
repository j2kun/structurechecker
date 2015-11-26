# a generic function to check a module for a hierarchy of nested attributes

class HierarchyTypeException(Exception):
   pass


def checkStructure(modules, hierarchyTree):
   errors = []
   moduleDict = dict((m.__name__, m) for m in modules)

   if type(hierarchyTree) is not dict:
      raise HierarchyTypeException("Entire hierarchy tree should be a dict")

   for name, attrs in sorted(hierarchyTree.items()):
      if name not in moduleDict:
         errors.append(name)
      else:
         moduleErrors = checkHierarchy(moduleDict[name], attrs, depth=name)
         if moduleErrors is not []:
            errors.extend(moduleErrors)

   return errors


def checkHierarchy(module, hierarchyTree, depth=""):
   if type(hierarchyTree) is list:
      return ["%s.%s" % (depth,x) for x in hierarchyTree if not hasattr(module, x)]

   if type(hierarchyTree) is dict:
      errors = []

      for attr, subattrs in sorted(hierarchyTree.items()):
         if hasattr(module, attr):
            submodule = getattr(module, attr)
            suberrors = checkHierarchy(submodule, subattrs, 
                           depth="%s.%s" % (depth, submodule.__name__))
            errors.extend(suberrors)
         else:
            errors.append("%s.%s" % (depth, attr))

      return errors
   else:
      raise HierarchyTypeException("Wrong type %r used in hierarchy at depth %r" % (type(hierarchyTree), depth))
