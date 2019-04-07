import angr
import claripy

state = proj.factory.entry_state()
sm=p.factory.simulation_manager(state)
sm=proj.factory.simulation_manager(state)
res=sm.explore(find=0x40106f,avoid=0x0000000000401028) 
print res.found[0].posix.dumps(0)

'''
./easyCpp
0000000987
4294966919
4294966686
4294966542
4294966453
4294966398  
4294966364
4294966343
4294966330
4294966322
4294966317
4294966314
4294966312
4294966311
4294966310
4294966310
You win!
Your flag is:flag{987-377-843-953-979-985}
'''
