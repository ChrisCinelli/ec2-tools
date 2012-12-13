from boto.ec2 import connect_to_region
import argparse



ec2  = connect_to_region('us-east-1')

def make_hosts_file(opts):

    instances = []
    reservations = ec2.get_all_instances()
    for r in reservations:
        for i in r.instances:
            instances.append(i)

    for i in instances:
        if i.public_dns_name:
            print "Host %s" % i.public_dns_name
            print "    IdentityFile %s/%s"  % (opts.id_file_dir,i.key_name)
            print "    User %s" % opts.user
            for extra in opts.extra_args:
                print "    %s" % extra

def main():

    parser = argparse.ArgumentParser("make an ssh hosts file for")
    parser.add_argument("--id-file-dir",default="~/.ssh",required=False)
    parser.add_argument("--user",default="ubuntu",required=False)
    parser.add_argument("--extra-args",type=str,action='append',default=[],required=False)
    make_hosts_file(parser.parse_args())

if __name__ == "__main__" : main()
    
