# Copyright Epic Games, Inc. All Rights Reserved.

import bpy
from send2ue.core.extension import ExtensionBase


class ExampleExtension(ExtensionBase):
    name = 'example'

    hello_property: bpy.props.StringProperty(default='Hello world')

    def draw_validations(self, dialog, layout):
        """
        Can be overridden to draw an interface for the extension under the validations tab.

        :param Send2UeSceneProperties self: The scene property group that contains all the addon properties.
        :param Send2UnrealDialog dialog: The dialog class.
        :param bpy.types.UILayout layout: The extension layout area.
        """
        row = layout.row()
        row.prop(self.extensions.example, 'hello_property')

    def pre_operation(self):
        """
        Defines the pre operation logic that will be run before the operation.

        :param Send2UeSceneProperties self: The scene property group that contains all the addon properties.
        """
        print('Before the Send to Unreal operation')
        self.unreal_mesh_folder_path = '/Game/example_extension/test/'

    def pre_validations(self):
        """
        Defines the pre validation logic that will be an injected operation.

        :param Send2UeSceneProperties self: The scene property group that contains all the addon properties.
        """
        print('Before Validations')
        # Setting this to False will terminate execution in the validation phase
        if self.extensions.example.hello_property != 'Hello world':
            self.validations_passed = False

    def pre_mesh_export(self):
        """
        Defines the pre mesh export logic that will be an injected operation.

        :param PropertyGroup self: The scene property group that contains all the addon properties.
        """
        print('Before Mesh Export')
        print(self.file_path)
        print(self.asset_name)

    def pre_animation_export(self):
        """
        Defines the pre animation export logic that will be an injected operation.

        :param PropertyGroup self: The scene property group that contains all the addon properties.
        """
        print('Before Animation Export')
        print(self.file_path)
        print(self.asset_name)

    def post_operation(self):
        """
        Defines the post operation logic that will be run after the operation.
        """
        print('After the Send to Unreal operation')