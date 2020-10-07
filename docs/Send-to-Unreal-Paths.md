---
layout: home
---

# Paths
## Video:
[![](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/videos/thumbnails/paths.png)](https://www.youtube.com/watch?v=oVIKQVbXgbY&list=PLZlv_N0_O1gZfQaN9qXynWllL7bzX8H3t&index=5)

## Text:

First, let's talk about the settings under the ‘Paths’ section. You'll see that there is this drop down, and it gives you three options: ‘Send to Unreal’, ‘Export to Disk’ or ‘Both’. 

![1](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/images/paths/1.png)

When using ‘Send to Unreal’ the paths are the relative paths from your open Unreal project that ‘Send to Unreal’ uses when it runs the import. The ‘Game’ folder is equivalent to the ‘Content’ folder you see in your open Unreal project.

![2](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/images/paths/2.png)![2.5](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/images/paths/2.5.png)

When using ‘Export to Disk’, the path is the full path to the folder where the files will be exported on disk.

![3](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/images/paths/3.png)![3.5](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/images/paths/3.5.png)

When using ‘Both’, it will export to the specified folders on disk and import to the specified folders in your project.

### Mesh Folder (Unreal):

This is the mesh import path. All your static and skeletal meshes will be imported to this location in your open unreal project.  


### Animation Folder (Unreal):

This is the animation import path. All your actions that are in an Armature object’s NLA strips will be imported to this location in your open Unreal Project.


### Skeleton Asset (Unreal):

This is the direct path to the Skeleton you want to import animation on. You can get this path by right-clicking on the skeleton asset in Unreal and selecting ‘Copy Reference’.

![4](https://blender-tools-documentation.s3.amazonaws.com/send-to-unreal/images/paths/4.png)

NOTE:

Animation only imports can also be done by leaving the Skeleton Asset path blank and having only a rig under the ‘Rig’ collection.  In this case, ‘Send to Unreal’ will try to import onto a Skeleton in the folder specified by ‘Mesh Folder (Unreal)’ that matches the name of the skeletal mesh plus ‘_Skeleton’.

### Mesh Folder (Disk):

This is the path to the folder where your mesh is exported to on disk. All your static and skeletal meshes will be exported to this location. The file names will match the object names in Blender.


### Animation Folder (Disk):

This is the path to the folder where your actions will be exported to on disk. All your actions that are in an Armature object’s NLA strips will be exported to this location. The file names will match the action names in Blender.