import open3d as o3d
#mesh = o3d.geometry.TriangleMesh.create_sphere()
#mesh.compute_vertex_normals()

mesh = o3d.io.read_triangle_mesh("stl/kipr.stl")
#mesh.compute_triangle_normals()
#mesh.compute_vertex_normals()
o3d.io.write_triangle_mesh("stl/kipr_test.obj", mesh, write_vertex_normals = False)
#o3d.visualization.draw(mesh, raw_mode=True)