import open3d as o3d

# NOTE: If on a Mac, you need to run `brew install libomp` before `pip install open3d`

if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud("./large_isolated.ply")
    # o3d.visualization.draw_geometries([pcd], mesh_show_wireframe=True)
    bbox = o3d.geometry.PointCloud.get_oriented_bounding_box(pcd)
    print(bbox.dimension)
