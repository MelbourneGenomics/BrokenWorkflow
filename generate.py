#!/usr/bin/env python2
import dxpy
from dxpy.app_builder import upload_applet
import argparse


def get_parser():
    parser = argparse.ArgumentParser('Generates a broken workflow')
    parser.add_argument('--project', help='The target project for the workflow', required=True)
    parser.add_argument('--folder', help='The target folder, within the project, for the workflow', required=True)
    parser.add_argument('--name', help='The name for the workflow (optional)', default='BrokenWorkflow', required=False)
    return parser


def main(project, folder, name):
    # Build the applet
    app_id, app_desc = upload_applet('.', None)
    app_handler = dxpy.DXApplet(app_id)

    # Build a workflow that uses that applet
    workflow = dxpy.new_dxworkflow(name=name, project=project, folder=folder)
    workflow.add_stage(app_id)

    # Delete the applet, to break the workflow
    app_handler.remove()

    return workflow.get_id()


if __name__ == '__main__':
    args = get_parser().parse_args()
    print(main(**vars(args)))
