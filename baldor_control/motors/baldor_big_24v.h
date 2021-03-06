//#define MAX_FREQ 5*2*PI //12V
#define MAX_FREQ 10*2*PI //24V
#define MIN_EXC_FREQ_PERC 0.1
#define MIN_EXC_VOLT 0.1f
#define MAX_EXC_VOLT 1.0f
#define RESOLVER_STATOR_OFFSET -30*2*PI/360

//#define P 0.01f //12V
#define P 0.03f //24V

//#define I 0.0001f //12V
#define I 0.00005f //24V

//#define D 0.1f //12V
#define D 0.5f //24V

#define P_MAX (87.0f*PI/180.0f)
#define I_MAX (87.0f*PI/180.0f)
#define D_MAX (87.0f*PI/180.0f)

#define PID_MAX (87.0f*PI/180.0f) //acceleration torque
