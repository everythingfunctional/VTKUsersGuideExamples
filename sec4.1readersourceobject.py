import vtk
from vtk.util.colors import tomato

part = vtk.vtkSTLReader()
part.SetFileName("../VTKdata/Data/42400-IDGH.stl")

partMapper = vtk.vtkPolyDataMapper()
partMapper.SetInputConnection(part.GetOutputPort())

partActor = vtk.vtkLODActor()
partActor.SetMapper(partMapper)

# Create the graphics structure
ren1 = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renederer, set the background and size
ren1.AddActor(partActor)
ren1.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200, 200)

iren.Initialize()
iren.Start()
