import bounce_app
import ib
import context
import util

if __name__ == '__main__':
    context.init()
    util.setupLogger()
    ib.main(bounce_app.BounceApp)
