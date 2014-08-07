import vtk
from vtk.util.colors import tomato

cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(8)

cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)

cylinderActor.GetProperty().SetColor(tomato)
cylinderActor.RotateX(30.0)
cylinderActor.RotateY(-45.0)

# Create the graphics structure
ren1 = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Add the actors to the renederer, set the background and size
ren1.AddActor(cylinderActor)
ren1.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200, 200)

# Associate the "u" keypress with a UserEvent and start the event loop
#iren.AddObserver(vtk.UserEvent(
iren.Initialize()
iren.Start()
